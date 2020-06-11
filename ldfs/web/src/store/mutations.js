import * as type from './types';

const mutations = {
  [type.SET_CHECK_INFO](state,data){
    state.check_data = data
  }
};

export default mutations
