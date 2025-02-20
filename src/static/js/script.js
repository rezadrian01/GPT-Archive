const initialize = () => {
  const initializeEventListenersActionModal = () => {
    const actionModals = document.getElementsByClassName("conv-action-btn");
    const actionModalOverlay = document.getElementsByClassName(
      "conv-action-modal-overlay"
    );
    for (let i = 0; i < actionModals.length; i++) {
      const actionModal = actionModals[i];
      const id = actionModal.id;
      const convId = id.slice(16);
      actionModal.addEventListener("click", (e) => {
        e.stopPropagation();
        toggleConvActionModal(convId);
      });
    }
    for (let i = 0; i < actionModals.length; i++) {
      const overlay = actionModalOverlay[i];
      const id = overlay.id;
      const convId = id.slice(26);
      overlay.addEventListener("click", (e) => {
        e.stopPropagation();
        toggleConvActionModal(convId);
      });
    }
  };

  // calling the function
  initializeEventListenersActionModal();
};
initialize();

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

const toggleConvActionModal = (convId) => {
  const modal = document.getElementById(`conv-action-modal-${convId}`);
  const overlay = document.getElementById(
    `conv-action-modal-overlay-${convId}`
  );

  if (!modal || !overlay) {
    console.error(`Modal or overlay not found for convId: ${convId}`);
    return;
  }

  if (
    modal.classList.contains("hidden") &&
    overlay.classList.contains("hidden")
  ) {
    // Modal
    modal.classList.remove("hidden");
    modal.classList.add("flex");

    // Overlay
    overlay.classList.remove("hidden");
    overlay.classList.add("block");
  } else {
    // Modal
    modal.classList.remove("flex");
    modal.classList.add("hidden");

    // Overlay
    overlay.classList.remove("block");
    overlay.classList.add("hidden");
  }
};

const handleClick = () => {
  console.log("Clicked");
};
