<template>
  <component :is="layout" />
  <Teleport to="body"> <ToastComponent /> </Teleport>
</template>

<script>
import { useRoute } from "vue-router";
import { computed } from "vue";
import BaseLayout from "@/layouts/BaseLayout.vue";
import EmptyLayout from "@/layouts/EmptyLayout.vue";
import ToastComponent from "@/components/ToastComponent.vue";

export default {
  components: {
    ToastComponent,
    BaseLayout,
    EmptyLayout,
  },
  setup() {
    const route = useRoute();

    const layout = computed(() => route.meta.layout ?? "EmptyLayout");

    return {
      layout,
    };
  },
};
</script>

<style lang="scss">
@import "@/assets/scss/global";

#app {
  height: 100%;
}
</style>
