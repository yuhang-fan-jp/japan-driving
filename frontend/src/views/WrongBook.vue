<template>
  <div>
    <h2>错题本</h2>

    <div v-for="q in list" :key="q.question_id">
      <p>{{ q.content }}</p>
      <img v-if="q.image_url" :src="q.image_url" width="200" />
      <p>正确答案：{{ q.correct_answer ? "对" : "错" }}</p>
      <p>解析：{{ q.explanation }}</p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import http from "../api/http";

const list = ref<any[]>([]);

onMounted(async () => {
  const res = await http.get("/quiz/wrong-questions");
  list.value = res.data;
});
</script>