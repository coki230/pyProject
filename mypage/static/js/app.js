//document.getElementById('recordBtn').addEventListener('click', function() {
//    navigator.mediaDevices.getUserMedia({ audio: true })
//        .then(stream => {
//            const mediaRecorder = new MediaRecorder(stream);
//            mediaRecorder.start();
//
//            const audioChunks = [];
//            mediaRecorder.addEventListener("dataavailable", event => {
//                audioChunks.push(event.data);
//            });
//
//            mediaRecorder.addEventListener("stop", () => {
//                const audioBlob = new Blob(audioChunks);
//                const audioUrl = URL.createObjectURL(audioBlob);
//                const audio = document.getElementById('audioPlayback');
//                audio.src = audioUrl;
//                // 设置5秒后播放
//                setTimeout(() => {
//                    audio.play();
//                }, 5000);
//            });
//
//            // 设置录制时间为5秒
//            setTimeout(() => {
//                mediaRecorder.stop();
//            }, 5000);
//        })
//        .catch(error => console.error('获取麦克风权限失败:', error));
//});


function blobToArrayBuffer(blob) {
        const audioContext = new AudioContext();
        const arrayBuffer = blob.arrayBuffer();
        const audioBuffer = audioContext.decodeAudioData(arrayBuffer);
        const float32Array = audioBuffer.getChannelData(0); // Assuming mono channel
        return float32Array;
}

document.getElementById('recordBtn').addEventListener('click', function() {
    navigator.mediaDevices.getUserMedia({ audio: true })
        .then(stream => {
            const mediaRecorder = new MediaRecorder(stream);
            mediaRecorder.start();

            let audioChunks = [];
            mediaRecorder.addEventListener("dataavailable", event => {
                audioChunks.push(event.data);
            });

            mediaRecorder.addEventListener("stop", () => {
                const audioBlob = new Blob(audioChunks);
                const audioBuffer = blobToArrayBuffer(audioBlob);
                sendAudioToServer(audioBuffer);
                audioChunks = [];
            });

            setTimeout(() => {
                mediaRecorder.stop();
            }, 5000); // 停止录音
        })
        .catch(error => console.error('获取麦克风权限失败:', error));
});

function sendAudioToServer(blob) {
    const formData = new FormData();
    formData.append('audio', blob);

    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.blob())
    .then(blob => {
        const audioUrl = URL.createObjectURL(blob);
        const audio = new Audio(audioUrl);
        audio.play();
    })
    .catch(error => console.error('Error:', error));
}


function test() {
    console.log(123)
    fetch('/play', {
        method: 'POST'
    })
    .then(response => response.blob())
    .then(blob => {
        const audioUrl = URL.createObjectURL(blob);
        const audio = new Audio(audioUrl);
        audio.play();
    })
    .catch(error => console.error('Error:', error));
}

function chat() {
    console.log(111)
    // 检查浏览器是否支持 getUserMedia
    if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
      // 请求麦克风权限
      navigator.mediaDevices.getUserMedia({ audio: true })
        .then(function(stream) {
          // 创建一个 AudioContext
//          const audioContext = new AudioContext();
          const audioContext = new (window.AudioContext || window.webkitAudioContext)({
            sampleRate: 16000
          });

          sampleRate = audioContext.sampleRate; // 获取音频的采样率
          console.log('sampleRate数据2222:', sampleRate);

          // 创建一个 MediaStreamAudioSourceNode
          const source = audioContext.createMediaStreamSource(stream);
          // 创建一个 ScriptProcessorNode 用于处理音频数据
          const processor = audioContext.createScriptProcessor(4096, 1, 1);

          // 用于存储音频数据的数组
          let audioData = [];

          // 连接节点
          source.connect(processor);
          processor.connect(audioContext.destination);

          // 处理音频数据
          processor.onaudioprocess = function(e) {
            // 获取输入缓冲区的数据
            const inputData = e.inputBuffer.getChannelData(0);
            // 将数据添加到数组中
            audioData = audioData.concat(Array.from(inputData));
          };

          // 设置一个定时器，在 5 秒后停止收集数据
          setTimeout(() => {
            // 断开处理器的连接，停止处理数据
            processor.disconnect();
            source.disconnect();
            // 处理或返回收集到的音频数据
            sendToServer(audioData)
            console.log('收集到的音频数据:', audioData);
            // 可以在这里添加更多的处理逻辑，例如发送到服务器等
          }, 2000);

        })
        .catch(function(err) {
          console.error('获取麦克风权限失败：', err);
        });
    } else {
      console.error('浏览器不支持 getUserMedia');
    }
}


function sendToServer(audioArray) {
    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ audioData: Array.from(audioArray) })
    })
    .then(response => response.blob())
    .then(blob => {
        const audioUrl = URL.createObjectURL(blob);
        const audio = new Audio(audioUrl);
        audio.play();
    })
    .catch(error => console.error('Error sending audio to server:', error));
}