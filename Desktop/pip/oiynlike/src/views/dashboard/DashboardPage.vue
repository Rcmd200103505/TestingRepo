<template>
  <div class="d-flex flex-column flex-grow-1">
    <div class="d-flex justify-space-between align-center">
      <img
        :src="require('@/assets/images/logo.png')"
        alt="logo"
        width="120px"
        height="auto"
      />
      <NotificationsDialog />
    </div>
    <TabsComponent class="my-5" :items="tabItems" />
    <router-view />
  </div>
</template>

<script>
import { computed } from "vue";
import TabsComponent from "@/components/TabsComponent.vue";
import NotificationsDialog from "@/components/NotificationsDialog.vue";

export default {
  components: { NotificationsDialog, TabsComponent },
  setup() {
    const tabItems = computed(() => [
      {
        text: "Рекомендации",
        type: "recommended",
        to: "/dashboard/recommended",
      },
      {
        text: "Мои игры",
        type: "user",
        to: "/dashboard/user",
      },
    ]);

    return {
      tabItems,
    };
  },
};
</script>
