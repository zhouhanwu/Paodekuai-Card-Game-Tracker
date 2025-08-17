# Audio helper functions for Streamlit

def get_audio_script():
    """Returns JavaScript code for audio playback"""
    return """
    <script>
    function playAudio() {
        // Create audio element
        const audio = new Audio('wocao.mp3');
        
        // Try to play the audio
        audio.play().catch(function(error) {
            console.log('Audio autoplay failed:', error);
            // Fallback: show a play button
            const playButton = document.createElement('button');
            playButton.textContent = '🔊 Play 俘了 Sound';
            playButton.style.cssText = 'position:fixed;top:60%;left:50%;transform:translate(-50%,-50%);z-index:10000;padding:10px 20px;background:red;color:white;border:none;border-radius:10px;cursor:pointer;';
            playButton.onclick = function() {
                audio.play();
                this.remove();
            };
            document.body.appendChild(playButton);
        });
    }
    
    // Execute when the script loads
    playAudio();
    </script>
    """

def get_audio_html():
    """Returns HTML with embedded audio and fallback"""
    return """
    <div style="position: fixed; top: 60%; left: 50%; transform: translate(-50%, -50%); z-index: 10000;">
        <audio id="fuAudio" controls style="display: none;">
            <source src="wocao.mp3" type="audio/mp3">
            Your browser does not support the audio element.
        </audio>
        <button onclick="document.getElementById('fuAudio').play()" 
                style="padding: 10px 20px; background: red; color: white; border: none; border-radius: 10px; cursor: pointer;">
            🔊 Play 俘了 Sound
        </button>
    </div>
    """
