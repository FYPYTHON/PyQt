import * as type from './types'

const action = {
  set_check_data({commit}, data) {
    commit(type.SET_CHECK_INFO, data);
  }
};
export default action
