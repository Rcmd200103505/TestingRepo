<template>
  <v-text-field
    placeholder="Пароль"
    variant="outlined"
    :type="isVisible ? 'text' : 'password'"
    density="comfortable"
    :model-value="modelValue"
    :append-inner-icon="isVisible ? 'far fa-eye-slash' : 'far fa-eye'"
    @click:append-inner="toggleVisibility"
    @update:model-value="$emit('update:model-value', $event)"
  />
</template>

<script>
import { ref } from "vue";

export default {
  props: {
    modelValue: {
      type: String,
      default: "",
    },
  },
  setup() {
    const isVisible = ref(false);

    function toggleVisibility() {
      isVisible.value = !isVisible.value;
    }

    return {
      isVisible,
      toggleVisibility,
    };
  },
};
</script>

<style lang="scss" scoped></style>
