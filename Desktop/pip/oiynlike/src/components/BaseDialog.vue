<template>
  <v-dialog v-model="dialog" transition="dialog-bottom-transition" fullscreen>
    <template v-slot:activator="{ props: activatorProps }">
      <slot name="activator" :activatorProps="activatorProps" />
    </template>
    <slot :close="close" />
  </v-dialog>
</template>

<script>
import { ref } from "vue";

export default {
  setup() {
    const dialog = ref(false);

    function close() {
      dialog.value = false;
    }

    return {
      dialog,
      close,
    };
  },
};
</script>
