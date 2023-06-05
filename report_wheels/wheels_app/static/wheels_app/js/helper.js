const buttons = document.querySelectorAll(
  ".add-btn, .add-dept-btn, .add-tra-ven-btn"
);

const overlay = document.querySelector(".overlay");
const closeButtons = document.querySelectorAll(".close-button");
const successOverlay = document.querySelector(".success-overlay");
const depOverlay = document.querySelector(".add-dept-overlay");
const travelVendorOverlay = document.querySelector(
  ".add-travel-vendor-overlay"
);

export function addBtnHandler() {
  buttons.forEach((button) => {
    button.addEventListener("click", function () {
      if (button.classList.contains("add-btn")) {
        overlay.classList.add("overlay-active");
      } else if (button.classList.contains("add-dept-btn")) {
        depOverlay.classList.add("overlay-active");
      } else if (button.classList.contains("add-tra-ven-btn")) {
        travelVendorOverlay.classList.add("overlay-active");
      }
    });
  });
}
export function closeModal() {
  const overlays = [overlay, successOverlay, depOverlay, travelVendorOverlay];

  overlays.forEach((overlayElement) => {
    if (overlayElement)
      overlayElement.addEventListener("click", function (event) {
        if (
          event.target === overlayElement ||
          Array.from(closeButtons).some((closeButton) =>
            closeButton.contains(event.target)
          )
        ) {
          overlayElement.classList.remove("overlay-active");
        }
      });
  });
}
// export function closeModal() {
//   overlay.addEventListener("click", function (event) {
//     handleCloseClick(event, overlay);
//   });

//   if (successOverlay) {
//     successOverlay.addEventListener("click", function (event) {
//       handleCloseClick(event, successOverlay);
//     });
//   }
//   depOverlay.addEventListener("click", function (event) {
//     handleCloseClick(event, depOverlay);
//   });
//   travelVendorOverlay.addEventListener("click", function (event) {
//     handleCloseClick(event, travelVendorOverlay);
//   });
// }
// function handleCloseClick(event, overlayElement) {
//   if (
//     event.target === overlayElement ||
//     Array.from(closeButtons).includes(event.target)
//   ) {
//     overlayElement.classList.remove("overlay-active");
//   }
// }
