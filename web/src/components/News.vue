<template>
  <!-- Контейнер карточек -->
  <div class="card__container">
    <!-- Карточки -->
    <div v-if="selectedNews">
      <button v-on:click="backToList">Назад</button>
      <div>
        <h1>{{ selectedNews.name }}</h1>
        <div v-html="selectedNews.description"></div>
      </div>
    </div>
    <div
      v-else
      v-for="item in items"
      :key="item.id"
      @click="showNews(item)"
      class="card"
    >
      <div class="thumbnail__container">
        <img class="thumbnail" :src="item.image" />
      </div>
      <div class="title-description__container">
        <p сlass="date">{{ item.date }}</p>
        <a class="title">{{ item.name }}</a>
        <div v-html="item.description" class="description"></div>
        <!-- <div class="description"> -->
        <!--     {{ item.description }}   -->
        <!-- </div> -->
        <p class="tags">
          <span v-for="tag in item.tags"> #{{ tag }} </span>
        </p>
        <p class="keywords">
          <span v-for="keyword in item.keywords"> #{{ keyword }} </span>
        </p>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import NewsDetails from "NewsDetails";

interface Tag {
  name: string;
}

interface Keywords {
  name: string;
}

interface News {
  id: number;
  date: string;
  name: string;
  description: string;
  tags: Tag[];
  keywords: Keywords[];
  image: string;
}

export default {
  data() {
    return {
      items: [] as News[],
      selectedNews: null,
    };
  },
  methods: {
    async fetchArticles() {
      const response = await fetch("http://localhost:8000/api/news");
      this.items = await response.json();
    },
    showNews(item) {
      //this.$emit("show-article", item.description);
      this.selectedNews = item;
      console.log(item);
    },
    backToList() {
      this.selectedNews = null;
    },
  },
  mounted() {
    this.fetchArticles();
  },
};
</script>

<style scoped>
.card__container {
  display: flex;
  flex-direction: column;
}
.card {
  display: flex;
  flex-direction: row;
  background-color: #fff;
  overflow: hidden;
  margin: 1em;
  border-radius: 1em;
  /* overflow-wrap: break-word; */
}
.thumbnail__container {
  width: 50%;
}
.thumbnail {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.title-description__container {
  margin: 1em;
}
.date {
  color: rgb(240, 242, 245);
}
.title {
  font-weight: bold;
}
.description {
}
@media only screen and (max-width: 720px) {
  .card {
    flex-direction: column !important;
  }
  .thumbnail__container {
    width: 100%;
  }
}
</style>
