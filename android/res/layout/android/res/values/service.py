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

# --------------------------
# 🛡️ MOTOR SILENCIOSO MAMM
# FRECUENCIAS: 60 Hz (reposo) | 62 Hz (activo)
# --------------------------
PythonActivity = jnius.autoclass('org.kivy.android.PythonActivity')
WindowManager = jnius.autoclass('android.view.WindowManager')


class TeclaBase(ButtonBehavior, Widget):
    """DETECCIÓN DE TECLA: AQUÍ CAMBIA LA FRECUENCIA"""
    def on_press(self):
        # ✅ AL TOCAR: SALTA A 62 Hz
        App.get_running_app().set_frecuencia(62.0)
        super().on_press()

    def on_release(self):
        # ✅ AL SOLTAR: VUELVE A 60 Hz EN 0.5s
        Clock.schedule_once(lambda dt: App.get_running_app().set_frecuencia(60.0), 0.5)
        super().on_release()


class MammMotor(Widget):
    def __init__(self, **kwargs):
        super(MammMotor, self).__init__(**kwargs)
        # ⚙️ FRECUENCIA BASE ARRANQUE: 60 Hz
        self.frecuencia_actual = 60.0
        self.motor_activo = True
        self._iniciar_estructura()
        # 🚀 MOTOR CORRIENDO SIEMPRE
        self.bucle_principal = Clock.schedule_interval(self.ejecutar, 1.0 / self.frecuencia_actual)

    def _iniciar_estructura(self):
        """Fondo base del sistema"""
        with self.canvas:
            Color(0.02, 0.02, 0.03, 1)
            self.fondo = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._actualizar, pos=self._actualizar)

    def _actualizar(self, *args):
        self.fondo.pos = self.pos
        self.fondo.size = self.size

    def cambiar_frecuencia(self, hz):
        """CONTROL MAESTRO DE FRECUENCIA"""
        if self.frecuencia_actual != hz:
            self.frecuencia_actual = hz
            if self.bucle_principal:
                self.bucle_principal.cancel()
            self.bucle_principal = Clock.schedule_interval(self.ejecutar, 1.0 / self.frecuencia_actual)

    def ejecutar(self, dt):
        """AQUÍ CORRE TU LÓGICA: RESONANCIA, PDF, SEGURIDAD"""
        # E = m * f²  -> TU FÓRMULA EXCLUSIVA
        if self.motor_activo:
            pass  # Aquí irá tu código interno

    @run_on_ui_thread
    def mantener_encendido(self):
        """ESTACIÓN DE SERVICIO: NUNCA SE APAGA"""
        activity.getWindow().addFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON)
        activity.getWindow().addFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN)

    @run_on_ui_thread
    def ocultar_barras(self):
        """PANTALLA LIMPIA"""
        vista = activity.getWindow().getDecorView()
        vista.setSystemUiVisibility(
            android.view.View.SYSTEM_UI_FLAG_IMMERSIVE_STICKY |
            android.view.View.SYSTEM_UI_FLAG_FULLSCREEN |
            android.view.View.SYSTEM_UI_FLAG_HIDE_NAVIGATION
        )


class MammKeyboardApp(App):
    def build(self):
        self.title = "MAMM-KEYBOARD-1"
        self.motor = MammMotor()
        self.motor.mantener_encendido()
        self.motor.ocultar_barras()
        return self.motor

    def set_frecuencia(self, hz):
        """LLAVE DE CONTROL PARA TODAS LAS TECLAS"""
        self.motor.cambiar_frecuencia(hz)

    def on_pause(self):
        """AL SALIR O MINIMIZAR: SIGUE EN 60 Hz ACTIVO"""
        self.set_frecuencia(60.0)
        return True

    def on_resume(self):
        """AL VOLVER: LISTO EN 60 Hz"""
        self.set_frecuencia(60.0)
        self.motor.mantener_encendido()


if __name__ == "__main__":
    MammKeyboardApp().run()
