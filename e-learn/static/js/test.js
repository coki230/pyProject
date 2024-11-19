function speak(text) {
    // 获取语音合成对象
    const synth = window.speechSynthesis;

    // 创建一个SpeechSynthesisUtterance对象
    const utterance = new SpeechSynthesisUtterance(text);

    // 可以设置语言、音调和速度等属性
    utterance.lang = 'zh-CN';  // 设置为中文
    utterance.pitch = 1;       // 音调 (0.1 到 2)
    utterance.rate = 1;        // 速度 (0.1 到 10)

    // 将文本传递给语音服务
    synth.speak(utterance);
}

function testSpeak(){
    // 使用函数
    speak('你好，世界！');
    console.log(222)
}