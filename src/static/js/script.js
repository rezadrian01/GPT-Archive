const insertConvModal = () => {
  const modal = document.getElementById("conv_modal");
  const modal_content = document.getElementById("conv_modal_content");
  const modal_close = document.getElementById("conv_modal_close");
  const modal_open = document.getElementById("conv_modal_open");

  modal_open.onclick = () => {
    modal.style.display = "block";
  };

  modal_close.onclick = () => {
    modal.style.display = "none";
  };

  window.onclick = (event) => {
    if (event.target == modal) {
      modal.style.display = "none";
    }
  };
};

const toggleInsertModal = () => {
  const insertModal = document.getElementById("insert-modal");
  const modalOverlay = document.getElementById("modal-overlay");
  if (insertModal.classList.contains("hidden")) {
    insertModal.classList.remove("hidden");
    modalOverlay.classList.remove("hidden");
  } else {
    insertModal.classList.add("hidden");
    modalOverlay.classList.add("hidden");
  }
};

const handleClick = () => {
  console.log("Clicked");
};
