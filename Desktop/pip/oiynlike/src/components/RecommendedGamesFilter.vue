<template>
  <div class="d-flex ga-3 overflow-x-auto hide-horizontal-scrollbar">
    <v-select
      :class="$style.select"
      rounded="xl"
      placeholder="Город"
      :items="CITY_LIST"
      variant="outlined"
      density="compact"
    ></v-select>
    <v-select
      rounded="xl"
      :class="[$style.select, $style.gameType]"
      class="flex-grow-1 flex-shrink-0"
      placeholder="Тип игры"
      :items="GAME_TYPES"
      variant="outlined"
      density="compact"
    ></v-select>
    <v-select
      :class="$style.select"
      rounded="xl"
      placeholder="Период"
      :items="PERIOD_TYPES"
      variant="outlined"
      density="compact"
    ></v-select>
  </div>
</template>

<script>
import { CITY_LIST, GAME_TYPES, PERIOD_TYPES } from "@/constants";

export default {
  setup() {
    return {
      CITY_LIST,
      GAME_TYPES,
      PERIOD_TYPES,
    };
  },
};
</script>

<style lang="scss" module>
.select {
  flex: 1 0 150px;

  &.gameType {
    flex-basis: 180px;
  }
}
</style>
