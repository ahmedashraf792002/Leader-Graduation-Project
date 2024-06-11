document.addEventListener("DOMContentLoaded", function() {
    const container = document.querySelector(".container");
    const uploadInput = document.getElementById("upload");
    const imageContainer = document.getElementById("image-container");
    const predictionBtn = document.getElementById("prediction-btn");

    container.addEventListener("mouseenter", function() {
        container.style.borderColor = "white";
    });

    container.addEventListener("mouseleave", function() {
        container.style.borderColor = "#ccc";
    });

    uploadInput.addEventListener("change", function(event) {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                const img = document.createElement("img");
                img.src = e.target.result;
                img.style.maxWidth = "100%";
                imageContainer.innerHTML = "";
                imageContainer.appendChild(img);
                // Show prediction button
                predictionBtn.style.display = "block";
                // Clear previous prediction result
                document.getElementById("result").textContent = "";
            };
            reader.readAsDataURL(file);
        }
    });

    predictionBtn.addEventListener("click", function() {
        const formData = new FormData();
        formData.append("file", uploadInput.files[0]);

        fetch("/predict", {
            method: "POST",
            body: formData
        })
        .then(response => response.text())
        .then(prediction => {
            // Display prediction result
            document.getElementById("result").textContent = "Prediction: " + prediction;
        })
        .catch(error => {
            console.error("Error:", error);
        });
    });
});
