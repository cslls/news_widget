<template>
  <div>
    <ul>
      <li v-for="item in items" :key="item.id">
        {{ item.name }}
      </li>
    </ul>
  </div>
</template>

<script>
import { ref, computed } from "vue";
import axios from "axios";

export default {
  data() {
    return {
      items: [],
    };
  },
  mounted() {
    axios.get("http://localhost:8000/api/news").then((response) => {
      this.items = response.data;
    });
  },
};
</script>
