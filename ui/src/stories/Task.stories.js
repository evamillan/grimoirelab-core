import Task from "./Task.vue";

// More on how to set up stories at: https://storybook.js.org/docs/writing-stories
export default {
  title: 'Example/Task',
  component: Task,
  tags: ['autodocs'],
  // argTypes: {
  //   size: { control: { type: 'select' }, options: ['small', 'medium', 'large'] },
  //   backgroundColor: { control: 'color' },
  // },

};

// More on writing stories with args: https://storybook.js.org/docs/writing-stories/args
export const Primary = {
  // args: {
  //   primary: true,
  //   label: 'Button',
  // },
};