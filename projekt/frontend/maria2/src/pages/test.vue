<template>
  <div class="q-pa-md" style="max-width: 300px">
    <div class="q-gutter-md">
      <q-select v-model="model" :options="options" label="Standard" />
      </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      myInput: '',
      model: null,
      options: [
        'Google', 'Facebook', 'Twitter', 'Apple', 'Oracle'
      ]
    }
  },
  methods: {
    handleClick () {
      this.myInput = 'clicked'
    }
  }
}
</script>
