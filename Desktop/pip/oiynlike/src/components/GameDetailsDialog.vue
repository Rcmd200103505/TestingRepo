<template>
  <BaseDialog v-model="isDialogShown">
    <template #activator="{ activatorProps }">
      <v-btn
        icon="fas fa-chevron-right"
        variant="plain"
        size="small"
        v-bind="activatorProps"
      />
    </template>
    <template #default="{ close }">
      <v-card>
        <v-card-title>
          <h1 class="text-h5 font-weight-bold" @click="close">
            <v-btn icon="fas fa-arrow-left-long" variant="flat" />
            Информация об игре
          </h1>
        </v-card-title>
        <v-card-text
          class="d-flex flex-column flex-grow-1 justify-space-between pb-4"
        >
          <div>
            <GameInfo :game="game" show-description />
          </div>
          <v-btn
            variant="flat"
            color="blue-darken-4"
            rounded="lg"
            size="large"
            class="text-body-2 w-100"
            :loading="isProcessing"
            @click="handleJoin"
          >
            Присоединиться
          </v-btn>
        </v-card-text>
      </v-card>
    </template>
  </BaseDialog>
</template>

<script>
import BaseDialog from "@/components/BaseDialog.vue";
import GameInfo from "@/components/GameInfo.vue";
import { ref } from "vue";
import { useToastStore } from "@/store/useToastStore";
import GameService from "@/api/service/gameService";

export default {
  components: { BaseDialog, GameInfo },
  props: {
    game: {
      type: Object,
      required: true,
    },
  },
  setup(props) {
    const isDialogShown = ref(false);

    const isProcessing = ref(false);

    async function handleJoin() {
      isProcessing.value = true;

      try {
        await GameService.joinGame(props.game._id);
        useToastStore().addToast("Вы успешно присоединились к игре!");
        isDialogShown.value = false;
      } catch (e) {
        useToastStore().addToast("Не удалось присоединиться к игре", "error");
      } finally {
        isProcessing.value = false;
      }
    }

    return { handleJoin, isProcessing, isDialogShown };
  },
};
</script>

<style lang="scss" scoped></style>
