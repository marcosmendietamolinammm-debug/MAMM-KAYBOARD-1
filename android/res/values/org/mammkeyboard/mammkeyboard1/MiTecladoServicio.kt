package org.mammkeyboard.mammkeyboard1

import android.inputmethodservice.InputMethodService
import android.view.LayoutInflater
import android.view.View
import android.view.inputmethod.EditorInfo
import android.view.KeyEvent
import android.util.Log

class MiTecladoServicio : InputMethodService() {

    private val TAG = "MAMM_KEYBOARD_SERVICE"
    private var vistaTeclado: View? = null

    override fun onCreateInputView(): View {
        Log.d(TAG, "Creando vista del teclado MAMM KEYBOARD 1")
        vistaTeclado = LayoutInflater.from(this).inflate(R.layout.teclado_layout, null)
        return vistaTeclado!!
    }

    override fun onStartInputView(editorInfo: EditorInfo?, restarting: Boolean) {
        super.onStartInputView(editorInfo, restarting)
        Log.i(TAG, "Teclado activado - Modo de entrada iniciado")
        window?.setWindowAnimations(android.R.style.Animation_InputMethod)
        setKeepScreenOn(true)
    }

    override fun onKeyDown(keyCode: Int, event: KeyEvent?): Boolean {
        when (keyCode) {
            KeyEvent.KEYCODE_BACK -> {
                Log.d(TAG, "Tecla atrás presionada")
            }
        }
        return super.onKeyDown(keyCode, event)
    }

    override fun onDestroy() {
        super.onDestroy()
        Log.w(TAG, "Servicio de teclado finalizado")
        vistaTeclado = null
    }
}

