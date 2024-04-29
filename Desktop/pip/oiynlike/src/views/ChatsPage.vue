<template>
  <div>
    <v-text-field
      placeholder="Поиск"
      variant="filled"
      rounded="lg"
      density="comfortable"
      prepend-inner-icon="fas fa-magnifying-glass"
      v-model="search"
      class="mb-4"
    />
    <h1 class="text-h4">Беседы</h1>
    <ul>
      <li v-for="chat in chats" :key="chat.id"></li>
    </ul>
  </div>
</template>

<script>
import { onMounted, ref } from "vue";
import GameService from "@/api/service/gameService";

export default {
  setup() {
    const search = ref("");
    const chats = ref([]);
    const isProcessing = ref(false);

    async function fetchChats() {
      isProcessing.value = true;

      try {
        chats.value = await GameService.fetchGamecards();
      } catch (e) {
        console.error(e);
      } finally {
        isProcessing.value = false;
      }
    }

    onMounted(() => {
      fetchChats();
    });

    return {
      search,
      chats,
    };
  },
};
</script>

<style lang="scss" scoped></style>
