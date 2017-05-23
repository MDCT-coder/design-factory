import { observable, action, runInAction } from 'mobx';
import request from '../utils/request';
import { postOptions, getOptions, deleteOptions } from '../utils/fetchOptions';


class FavoriteObjectStore {
  @observable allFavoriteObject = {};

  @action fetchAll = async () => {
    const { data } = await request('api/favorite-object/', { ...getOptions });
    runInAction(() => {
      const newData = {};
      for (const object of data) {
        newData[object.material.id] = object.material;
      }
      this.allFavoriteObject = newData;
    });
  };

  @action post = async (payload) => {
    const { err } = await request('/api/favorite-object/', { ...postOptions, ...payload });
    if (!err) {
      runInAction(() => {
        this.fetchAll();
      });
    }
    return {
      err
    }
  };

  @action del = async (payload) => {
    const { err } = await request('/api/favorite-object/:id/', { ...deleteOptions, ...payload });
    if (!err) {
      runInAction(() => {
        this.fetchAll();
      });
    }
  }
}

export default new FavoriteObjectStore();
