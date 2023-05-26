<template>
  <div>
    <ul>
      <li v-for="item in items" :key="item.id">
        {{ item.name }}
      </li>
    </ul>
  </div>
</template>

<script lang="ts">
import axios, { AxiosResponse } from "axios";

interface News {
  id: number;
  name: string;
}

export default {
  data() {
    return {
      items: [] as News[],
    };
  },
  mounted() {
    axios
      .get<News[]>("http://localhost:8000/api/news")
      .then((response: AxiosResponse<News[]>) => {
        this.items = response.data;
      });
  },
};
</script>
