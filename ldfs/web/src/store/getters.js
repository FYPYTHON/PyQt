import state from "./state";

const getters = {
  getCheckData: (state) => {
    console.log(state.check_data);
    return state.check_data
  },
};
export default getters
