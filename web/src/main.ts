import { createApp } from "vue";
import CKEditor from "@ckeditor/ckeditor5-vue";
import "boxicons";
import App from "./App.vue";
import "./assets/css/style.css";

createApp(App).use(CKEditor).mount("#app");

/* TODO:
 * Переименовать name->title, description->content, image->thumbnail
 * Сделать вывод названия и обложки
 * Сделать вывод полного текста статьи и картинок при клике на новость
 * Сделать кнопки редактирование, добавление, вход
 * Сделать вывод из CKEditor в content
 * */
