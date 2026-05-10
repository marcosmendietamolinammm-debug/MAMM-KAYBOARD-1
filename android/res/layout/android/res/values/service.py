# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivy.clock import Clock
from kivy.uix.behaviors import ButtonBehavior
from android import activity
from android.runnable import run_on_ui_thread
import android.view
import jnius

PythonActivity = jnius.autoclass('org.kivy.android.PythonActivity')
InputMethodManager = jnius.autoclass('android.view.inputmethod.InputMethodManager')
Context = jnius.autoclass('android.content.Context')
WindowManager = jnius.autoclass('android.view.WindowManager')


class TeclaBase(ButtonBehavior, Widget):
    """Clase base para todas las teclas: DETECTA EL TOQUE Y CAMBIA FRECUENCIA"""
    def on_press(self):
        # ✅ AL APLASTAR CUALQUIER TECLA: ACTIVAR 62 Hz
        App.get_running_app().establecer_frecuencia(62.0)
        super().on_press()

    def on_release(self):
        # ✅ AL SOLTAR / DEJAR DE USAR: VOLVER A 60 Hz
        Clock.schedule_once(lambda dt: App.get_running_app().establecer_frecuencia(60.0), 0.5)
        super().on_release()


class MammKeyboardService(Widget):
    def __init__(self, **kwargs):
        super(MammKeyboardService, self).__init__(**kwargs)
        self.frecuencia_actual = 60.0  # ⚙️ FRECUENCIA BASE INICIAL: 60 Hz
        self._init_motor()
        self._ciclo_activo = Clock.schedule_interval(self._ejecutar_motor, 1.0 / self.frecuencia_actual)

    def _init_motor(self):
        with self.canvas:
            Color(0.02, 0.02, 0.03, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def _ejecutar_motor(self, dt):
        """Bucle principal que corre a la frecuencia definida"""
        # Aquí corre tu lógica de resonancia, escaneo, generación PDF, etc.
        pass

    def cambiar_frecuencia_motor(self, hz):
        """Controlador maestro: 60 Hz reposo | 62 Hz activo"""
        if self.frecuencia_actual != hz:
            self.frecuencia_actual = hz
            if self._ciclo_activo:
                self._ciclo_activo.cancel()
            self._ciclo_activo = Clock.schedule_interval(self._ejecutar_motor, 1.0 / self.frecuencia_actual)

    @run_on_ui_thread
    def mantener_activo(self):
        activity.getWindow().addFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON)
        activity.getWindow().addFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN)

    @run_on_ui_thread
    def ocultar_barras_sistema(self):
        vista = activity.getWindow().getDecorView()
        vista.setSystemUiVisibility(
            android.view.View.SYSTEM_UI_FLAG_IMMERSIVE_STICKY |
            android.view.View.SYSTEM_UI_FLAG_FULLSCREEN |
            android.view.View.SYSTEM_UI_FLAG_HIDE_NAVIGATION |
            android.view.View.SYSTEM_UI_FLAG_LAYOUT_STABLE |
            android.view.View.SYSTEM_UI_FLAG_LAYOUT_FULLSCREEN
        )


class MammKeyboardApp(App):
    def build(self):
        self.title = "MAMM KEYBOARD 1"
        self.service = MammKeyboardService()
        self.service.mantener_activo()
        self.service.ocultar_barras_sistema()
        return self.service

    def establecer_frecuencia(self, hz):
        """LLAVE MAESTRA: LLAMADA DESDE CUALQUIER TECLA"""
        self.service.cambiar_frecuencia_motor(hz)

    def on_pause(self):
        # ✅ AL MINIMIZAR: MANTENER 60 Hz (ESTACIÓN DE SERVICIO ACTIVA)
        self.establecer_frecuencia(60.0)
        return True

    def on_resume(self):
        # ✅ AL VOLVER: ARRANCA EN 60 Hz HASTA QUE TOQUES
        self.establecer_frecuencia(60.0)
        self.service.mantener_activo()
        self.service.ocultar_barras_sistema()


if __name__ == "__main__":
    MammKeyboardApp().run()
