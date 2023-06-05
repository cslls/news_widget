<template>
  <div>
    <component :is="editor"></component>
  </div>
</template>

<script>
import Editor from "./Editor.vue";

export default {
  components: {
    Editor,
  },
  data() {
    return {
      editor: "Editor",
    };
  },
};
</script>
