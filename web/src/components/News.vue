<template>
  <!-- Контейнер карточен -->
  <div class="card__container">
    <!-- Карточки -->
    <div v-for="n in 10" class="card">
      <img
        class="thumbnail"
        src="https://images.unsplash.com/photo-1684654488308-2229de99e7a6?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1470&q=80"
      />
      <div class="title-description__container">
        <a class="title" href="#">Куда поехать на море в 2023 году недорого</a>
        <p class="description">{{ desc }}</p>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import axios, { AxiosResponse } from "axios";

interface News {
  id: number;
  name: string;
  description: string;
}

export default {
  data() {
    let desc: string = `Отдых за границей у моря не всегда означает большие траты, а иногда
          понежиться две недели на пляже и увидеть интересные
          достопримечательности в другой стране дешевле, чем провести то же
          время на русском юге.`;
    desc = desc.substring(0, 200).trim() + "...";
    return {
      desc,
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

<style>
.card__container {
  display: flex;
  flex-direction: column;
}
.card {
  display: flex;
  background-color: #fff;
  overflow: hidden;
  margin: 1em;
  border-radius: 1em;
  /* overflow-wrap: break-word; */
}
.thumbnail {
  width: 40%;
}
.title-description__container {
  margin: 1em;
}
.title {
  font-weight: bold;
}
.description {
}
</style>
