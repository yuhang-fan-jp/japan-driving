<template>
  <div class="card" @click="go">
    <div class="card-title">错题复习</div>
    <div class="card-desc">针对薄弱点重点练习</div>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from "vue-router";
const router = useRouter();

const go = () => {
  router.push("/wrong");
};
</script>

<style scoped>
@import "./card.css";
</style>
