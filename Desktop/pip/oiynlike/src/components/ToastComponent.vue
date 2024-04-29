<template>
  <v-fade-transition>
    <div
      class="d-flex flex-column ga-5 position-fixed w-100 pa-5"
      :class="[$style.wrapper, { [$style.visible]: toasts.length }]"
    >
      <v-fade-transition group>
        <v-alert
          v-for="toast in toasts"
          :key="toast.id"
          :type="toast.type || 'success'"
          :model-value="true"
        >
          <div class="d-flex justify-space-between align-center">
            <span>{{ toast.message }}</span>
            <v-btn
              variant="text"
              icon="fas fa-close"
              @click="handleRemove(toast)"
            />
          </div>
        </v-alert>
      </v-fade-transition>
    </div>
  </v-fade-transition>
</template>

<script>
import { useToastStore } from "@/store/useToastStore";
import { storeToRefs } from "pinia";

export default {
  setup() {
    const toastStore = useToastStore();
    const { toasts } = storeToRefs(toastStore);

    function handleRemove(toast) {
      toastStore.removeToast(toast.id);
    }

    return {
      toasts,
      handleRemove,
    };
  },
};
</script>

<style lang="scss" module>
.wrapper {
  top: 0;
  left: 0;

  &.visible {
    z-index: 3000;
  }
}
</style>
