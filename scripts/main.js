// Array to store images
let images = [];

// Maximum number of images to display
const maxImages = 20;

// Function to add a new image
function addImage(src) {
  if (images.length >= maxImages) {
    // If maximum number of images is reached, remove the first one
    images.shift();
  }
  let img = new Image();
  img.onload = function() {
    // Resize the image
    const desiredWidth = 180; // Adjust as needed
    const desiredHeight = 180; // Adjust as needed
    img.width = desiredWidth;
    img.height = desiredHeight;

    images.push(img);
    drawImages();
  };
  img.src = src;
}

// Function to draw images on the canvas
function drawImages() {
  const canvas = document.getElementById('canvas');
  const ctx = canvas.getContext('2d');
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  images.forEach(function(img) {
    // Generate random position
    let x = Math.random() * (canvas.width - img.width);
    let y = Math.random() * (canvas.height - img.height);
    ctx.drawImage(img, x, y, img.width, img.height); // Draw with image's own width and height
  });
}

// Add image URLs here
const imageUrls = [
  '/silhouette_1.png',
  '/silhouette_2.png',
  '/silhouette_3.png',
  '/silhouette_4.png',
  '/silhouette_5.png',
  '/silhouette_6.png',
  '/silhouette_7.png',
  '/silhouette_8.png',
  '/silhouette_9.png',
  '/silhouette_10.png',
  '/silhouette_11.png',
  '/silhouette_12.png',
  '/silhouette_13.png',
  '/silhouette_14.png',
  '/silhouette_15.png',
  '/silhouette_16.png',
  '/silhouette_17.png',
  '/silhouette_18.png',
  '/silhouette_19.png',
  '/silhouette_20.png',
];

// Load all images
imageUrls.forEach(function(url) {
  addImage(url);
});

// Set canvas size to match viewport dimensions
const canvas = document.getElementById('canvas');
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;