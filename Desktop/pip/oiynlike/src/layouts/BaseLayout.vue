<template>
  <main
    :class="$style.wrapper"
    class="px-6 pt-6 overflow-x-hidden position-relative h-100 d-flex flex-column"
  >
    <router-view />
    <TheBottomNav :class="$style.nav" class="position-fixed w-100" />
  </main>
</template>

<script>
import TheBottomNav from "@/components/TheBottomNav.vue";

export default {
  components: { TheBottomNav },
  setup() {
    return {};
  },
};
</script>

<style lang="scss" module>
.wrapper {
  padding-bottom: 81px;
}

.nav {
  max-height: 57px;
  bottom: 0;
  left: 0;
}
</style>
