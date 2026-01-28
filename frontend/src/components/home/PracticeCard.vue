<template>
  <div class="card" @click="go">
    <div class="card-title">知识练习</div>
    <div class="card-desc">50 题判断题，强化记忆</div>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from "vue-router";
const router = useRouter();

const go = () => {
  router.push("/practice");
};
</script>

<style scoped>
@import "./card.css";
</style>
