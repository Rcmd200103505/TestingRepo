<template>
  <ul class="d-flex flex-column ga-5">
    <template v-if="!isProcessing">
      <li v-for="item in items" :key="item.id">
        <v-card class="mx-auto rounded" max-width="400">
          <v-img
            class="align-end text-white"
            height="150"
            src="https://cdn.vuetifyjs.com/images/cards/docks.jpg"
            cover
          />
          <v-card-item>
            <GameInfo :game="item">
              <template #join>
                <GameDetailsDialog :game="item" />
              </template>
            </GameInfo>
          </v-card-item>
        </v-card>
      </li>
    </template>
    <template v-else>
      <v-skeleton-loader
        v-for="idx in 5"
        :key="idx"
        class="mx-auto border w-100"
        max-width="400"
        type="image, article"
      />
    </template>
  </ul>
</template>

<script>
import GameInfo from "@/components/GameInfo.vue";
import GameDetailsDialog from "@/components/GameDetailsDialog.vue";

export default {
  components: { GameDetailsDialog, GameInfo },
  props: {
    isProcessing: {
      type: Boolean,
      default: false,
    },
    items: {
      type: Array,
      default: () => [],
    },
  },
};
</script>
