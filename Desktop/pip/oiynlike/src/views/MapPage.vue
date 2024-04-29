<template>
  <div :class="$style.container" class="d-flex flex-column position-relative">
    <l-map
      ref="mapRef"
      v-model:zoom="zoom"
      :center="[43.238949, 76.889709]"
      :class="$style.map"
    >
      <l-tile-layer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        layer-type="base"
        name="OpenStreetMap"
      />
      <l-marker
        v-for="place in placeList"
        :key="place.name"
        :lat-lng="place.coordinates"
      >
        <l-popup>
          <div class="text-h6">{{ place.name }}</div>
          <div class="text-body-1">{{ place.address }}</div>
        </l-popup>
      </l-marker>
    </l-map>
    <div
      class="rounded-xl w-100 bg-white flex-grow-1 text-center position-absolute pa-3 pt-1 border-b"
      :class="$style.open"
      @click="sheet = true"
    >
      <v-icon icon="fas fa-minus" color="grey-lighten-1" size="x-large" />
      <v-text-field
        class="mt-4"
        placeholder="Поиск"
        variant="filled"
        rounded="lg"
        prepend-inner-icon="fas fa-magnifying-glass"
        density="comfortable"
        v-model="search"
        @input="onSearchInput"
      />
    </div>
    <v-bottom-sheet v-model="sheet" height="70%">
      <v-card
        class="text-center"
        height="100%"
        rounded="xl"
        :class="$style.sheetCard"
      >
        <v-icon
          icon="fas fa-minus"
          color="grey-lighten-1"
          size="x-large"
          class="mx-auto"
        />
        <v-card-text>
          <v-text-field
            placeholder="Поиск"
            variant="filled"
            rounded="lg"
            prepend-inner-icon="fas fa-magnifying-glass"
            density="comfortable"
            v-model="search"
          />
          <div class="text-h6 text-left mb-4">
            {{ search.length > 0 ? "Резльутаты поиска" : "Рекомендации" }}
          </div>
          <div v-if="search.length > 0 && !placeList.length">
            По вашему запросу ничего не найдено :(
          </div>
          <ul v-else class="text-left d-flex flex-column ga-4">
            <li
              v-for="place in placeList"
              :key="place.address"
              class="pa-3 elevation-1 rounded-lg"
            >
              <div class="text-body-1">{{ place.name }}</div>
              <div class="text-caption">
                <v-icon
                  size="x-small"
                  icon="fas fa-star"
                  color="yellow-darken-1"
                  class="mr-1"
                />
                <span>{{ place.rating }}</span>
              </div>
              <div class="text-body-2">{{ place.address }}</div>
            </li>
          </ul>
        </v-card-text>
      </v-card>
    </v-bottom-sheet>
  </div>
</template>

<script>
import "leaflet/dist/leaflet.css";
import { LMap, LTileLayer, LMarker, LPopup } from "@vue-leaflet/vue-leaflet";
import { computed, ref } from "vue";
import { PLACE_LIST } from "@/constants";

export default {
  components: {
    LMap,
    LTileLayer,
    LMarker,
    LPopup,
  },
  setup() {
    const mapRef = ref(null);
    const zoom = ref(12);
    const coordinates = [50, 50];
    const search = ref("");

    const placeList = computed(() =>
      search.value.length > 0
        ? PLACE_LIST.filter(
            (place) =>
              place.name.toLowerCase().includes(search.value.toLowerCase()) ||
              place.address.toLowerCase().includes(search.value.toLowerCase())
          )
        : PLACE_LIST
    );

    const sheet = ref(false);

    function onSearchInput() {
      sheet.value = true;
    }

    return {
      mapRef,
      zoom,
      coordinates,
      placeList,
      sheet,
      search,
      onSearchInput,
    };
  },
};
</script>

<style lang="scss" module>
.map {
  z-index: 1;
}

.open {
  z-index: 2;
  bottom: 0;
  left: 0;
}

.open,
.sheetCard {
  border-bottom-left-radius: 0 !important;
  border-bottom-right-radius: 0 !important;
}

.container {
  height: 100vh;
  margin: -24px;
}
</style>
