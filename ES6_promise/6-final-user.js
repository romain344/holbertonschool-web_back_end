import signUpUser from './4-user-promise.js';
import uploadPhoto from './5-photo-reject.js';

export default function handleProfileSignup(firstName, lastName, filename) {
    return Promise.allSettled([
        uploadPhoto(filename),
        signUpUser(firstName, lastName)
    ]) .then((results) =>
    results.map((r) => ({
      status: r.status,
      value: r.value || r.reason,
    }))
  );
}