<template>
  <nav
    class="px-6 py-4 bg-white elevation-2 d-flex justify-space-between align-center"
  >
    <router-link
      v-for="link in links"
      :key="link.to"
      :to="link.to"
      v-slot="{ isActive }"
    >
      <v-icon
        :icon="link.icon"
        :color="isActive ? 'blue-darken-4' : 'grey-darken-2'"
      />
    </router-link>
  </nav>
</template>

<script>
import { computed } from "vue";

export default {
  setup() {
    const links = computed(() => [
      {
        to: "/dashboard",
        icon: "fas fa-gamepad",
      },
      {
        to: "/map",
        icon: "fas fa-earth-americas",
      },
      {
        to: "/chats",
        icon: "far fa-comment-dots",
      },
      {
        to: "/users",
        icon: "fas fa-users",
      },
      {
        to: "/calendar",
        icon: "far fa-calendar",
      },
      {
        to: "/profile",
        icon: "fas fa-user",
      },
    ]);

    return { links };
  },
};
</script>

<style lang="scss" scoped></style>
