<template>
  <RecommendedGamesFilter />
  <GamesList :items="gamecards" :isProcessing="isProcessing" />
</template>

<script>
import GamesList from "@/components/GamesList.vue";
import RecommendedGamesFilter from "@/components/RecommendedGamesFilter.vue";
import { onMounted, ref } from "vue";
import GameService from "@/api/service/gameService";

export default {
  components: { RecommendedGamesFilter, GamesList },
  setup() {
    const isProcessing = ref(false);
    const gamecards = ref([]);

    async function fetchGamecards() {
      isProcessing.value = true;
      try {
        gamecards.value = await GameService.fetchRecommendedGamecards();
      } catch (e) {
        console.error(e);
      } finally {
        isProcessing.value = false;
      }
    }

    onMounted(() => {
      fetchGamecards();
    });

    return {
      gamecards,
      isProcessing,
    };
  },
};
</script>

<style lang="scss" scoped></style>
