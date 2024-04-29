import { ref } from "vue";
import { defineStore } from "pinia";

export const useToastStore = defineStore("toast", () => {
  const toasts = ref([]);

  function addToast(
    message,
    type = "success",
    { timeout } = { timeout: 3000 }
  ) {
    const toast = { id: Date.now(), message, type };
    toasts.value.push(toast);

    setTimeout(() => {
      removeToast(toast.id);
    }, timeout);
  }

  function removeToast(id) {
    toasts.value = toasts.value.filter((toast) => toast.id !== id);
  }

  return {
    toasts,
    addToast,
    removeToast,
  };
});
