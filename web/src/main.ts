import { createApp } from "vue";
import CKEditor from "@ckeditor/ckeditor5-vue";
import "./assets/css/style.css";
import App from "./App.vue";

createApp(App).use(CKEditor).mount("#app");
