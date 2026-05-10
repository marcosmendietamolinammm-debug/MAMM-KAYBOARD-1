package org.mammkeyboard.mammkeyboard1

import android.inputmethodservice.InputMethodService
import android.view.LayoutInflater
import android.view.View
import android.view.inputmethod.EditorInfo
import android.view.KeyEvent
import android.util.Log

/**
 * 🔌 SERVICIO PRINCIPAL DE TECLADO - MAMM KEYBOARD 1
 * Desarrollado por: Marcos Abel Mendieta Molina
 * Versión: 1.0.3 | Android 16 / API36
 * Propósito: Conectar el sistema Android con tu motor Kivy
 */
class MiTecladoServicio : InputMethodService() {

    // Etiqueta para logs
    private val TAG = "MAMM_KEYBOARD_SERVICE"
    private var tecladoVista: View? = null

    override fun onCreateInputView(): View {
        Log.d(TAG, "✅ Creando vista del teclado - MAMM KEYBOARD 1")
        
        // Inflamos tu diseño XML (el que configuramos en layout/teclado_layout.xml)
        tecladoVista = LayoutInflater.from(this).inflate(R.layout.teclado_layout, null)
        
        return tecladoVista!!
    }

    override fun onStartInputView(editorInfo: EditorInfo?, restarting: Boolean) {
        super.onStartInputView(editorInfo, restarting)
        Log.i(TAG, "⌨️ Teclado activado - Modo: ${editorInfo?.inputType}")
        
        // 🔒 Mantener activo el motor de resonancia (tu tecnología)
        setKeepScreenOn(true)
    }

    override fun onKeyDown(keyCode: Int, event: KeyEvent?): Boolean {
        // 🛡️ Captura de teclas especiales si es necesario
        when (keyCode) {
            KeyEvent.KEYCODE_BACK -> {
                Log.d(TAG, "🔙 Tecla atrás presionada")
                return super.onKeyDown(keyCode, event)
            }
        }
        return super.onKeyDown(keyCode, event)
    }

    override fun onDestroy() {
        super.onDestroy()
        Log.w(TAG, "⚠️ Servicio de teclado finalizado")
        tecladoVista = null
    }
}

