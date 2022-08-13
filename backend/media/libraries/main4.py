import java.util.concurrent.Executor
import android.annotation.SuppressLint

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.core.content.ContextCompat
import
com.example.fingerprintauth.databinding.ActivityMainBi
nding


class MainActivity:
    AppCompatActivity() {
        private lateinit var binding: ActivityMainBinding
        private lateinit var executor: Executor
        private lateinit var biometricPrompt:
        androidx.biometric.BiometricPrompt
        private lateinit var promptInfo:
        androidx.biometric.BiometricPrompt.PromptInfo
        override fun onCreate(savedInstanceState: Bundle?) {
            super.onCreate(savedInstanceState)
            binding = ActivityMainBinding.inflate(layoutInflater)
            setContentView(binding.root)
            executor = ContextCompat.getMainExecutor(this)
            biometricPrompt
            = androidx.biometric.BiometricPrompt(this@MainActivity,

                                                 executor, object: androidx.biometric.BiometricPrompt.Aut
                                                 henticationCallback(){
                                                     @ SuppressLint("SetTextI18n")
                                                     override fun onAuthenticationError(errorCode: Int,
                                                                                        errString: CharSequence) {
                                                         super.onAuthenticationError(
                                                             errorCode, errString)
                                                         binding.Authstatus.text="Error, $errString"
                                                     }
                                                     @ SuppressLint("SetTextI18n")
                                                     override fun onAuthenticationSucceeded(result:
                                                                                            androidx.biometric.BiometricPrompt.AuthenticationResul
                                                                                            t) {
                                                         super.onAuthenticationSucceeded(
                                                             result)
                                                         binding.Authstatus.text="Successful auth"
                                                     }
                                                     @ SuppressLint("SetTextI18n")
                                                     override fun onAuthenticationFailed() {
                                                         super.onAuthenticationFailed()
                                                         binding.Authstatus.text="Authentication Failed"
                                                     }
                                                 })

            promptInfo =
            androidx.biometric.BiometricPrompt.PromptInfo.Builder()
            .setTitle("Biometric Authentication")
            .setSubtitle("Login using fingerprint or face")
            .setNegativeButtonText("Cancel")
            .build()
            binding.Authbtn.setOnClickListener {
                biometricPrompt.authenticate(promptInfo)
            }
        }
    }
