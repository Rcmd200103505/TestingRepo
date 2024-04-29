<template>
  <BaseDialog>
    <template #activator="{ activatorProps }">
      <v-btn icon="far fa-bell" variant="flat" v-bind="activatorProps" />
    </template>
    <template #default="{ close }">
      <v-card class="flex-grow-1">
        <v-card-title>
          <h1 class="text-h5 font-weight-bold" @click="close">
            <v-btn icon="fas fa-arrow-left-long" variant="flat" />
            Уведомления
          </h1>
        </v-card-title>
        <v-card-item class="flex-grow-1 pb-5">
          <ul v-if="notifications.length"></ul>
          <div
            v-else
            class="d-flex flex-column align-center text-center flex-grow-1 justify-center"
          >
            <img
              :src="require('@/assets/images/no-games.svg')"
              alt="no games"
              width="100"
            />
            <h2 class="text-h5">
              У вас пока нет <br />
              уведомлений
            </h2>
          </div>
        </v-card-item>
      </v-card>
    </template>
  </BaseDialog>
</template>

<script>
import { onMounted, ref } from "vue";
import BaseDialog from "@/components/BaseDialog.vue";

export default {
  components: { BaseDialog },
  setup() {
    const isProcessing = ref(false);
    const notifications = ref([]);

    async function fetchNotifications() {
      isProcessing.value = true;

      try {
        //
      } catch (e) {
        console.error(e);
      } finally {
        isProcessing.value = false;
      }
    }

    onMounted(() => {
      fetchNotifications();
    });

    return {
      isProcessing,
      notifications,
    };
  },
};
</script>
