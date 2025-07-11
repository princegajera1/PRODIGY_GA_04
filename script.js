
async function translateImage() {
  const fileInput = document.getElementById('imageInput');
  const outputImage = document.getElementById('outputImage');

  if (!fileInput.files[0]) {
    alert("Please select an image first!");
    return;
  }

  const formData = new FormData();
  formData.append("image", fileInput.files[0]);

  outputImage.src = "";
  outputImage.alt = "Generating...";

  try {
    const response = await fetch("http://127.0.0.1:5000/translate", {
      method: "POST",
      body: formData
    });

    const data = await response.json();

    if (data.error) {
      outputImage.alt = "❌ Error: " + data.error;
    } else {
      outputImage.src = data.url;
    }
  } catch (err) {
    outputImage.alt = "❌ Network Error";
  }
}
