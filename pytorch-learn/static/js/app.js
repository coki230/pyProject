function handleDrop(event, element) {
    event.preventDefault();
    element.classList.remove('highlight');
    document.querySelector('.file-input').files = event.dataTransfer.files;
    handleFileChange(event);
}

function handleFileChange(event) {
    var files = event.target.files || event.dataTransfer.files;
    if (files.length > 0) {
        var file = files[0]; // Assuming only one file is selected
        var reader = new FileReader();
        reader.onload = function(e) {
            document.getElementById('preview').src = e.target.result;
            document.getElementById('preview').style.display = 'block';
        };
        reader.readAsDataURL(file);
    }
}

function submitFiles() {
    var fileInput = document.querySelector('.file-input');
    if (fileInput.files.length > 0) {
        var formData = new FormData();
        formData.append('image', fileInput.files[0]);  // Assuming only one file is selected

        fetch('/upload', {
            method: 'POST',
            body: formData,
        })
        .then(response => response.text())
        .then(data => {
            document.querySelector('.result').textContent = data;
        })
        .catch(error => {
            document.querySelector('.result').textContent = 'Upload failed';
        });
    } else {
        document.querySelector('.result').textContent = 'Please select a file first.';
    }
}