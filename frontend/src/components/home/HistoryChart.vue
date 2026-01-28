<template>
  <div class="card history">
    <div class="card-title">历史记录</div>
    <div class="chart-placeholder">
      得分 & 用时趋势图（待接入）
    </div>
  </div>
</template>

<script setup lang="ts">
// 后面这里会接 ECharts
</script>

<style scoped>
@import "./card.css";

.history {
  grid-column: span 2;
}

.chart-placeholder {
  height: 160px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #999;
  font-size: 14px;
  border: 1px dashed #ddd;
  border-radius: 10px;
}
</style>
