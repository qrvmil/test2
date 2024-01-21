import { useForm } from 'react-hook-form';
import axios from 'axios';
import Form from 'react-bootstrap/Form';
import { useNavigate } from 'react-router-dom';


function Register() {
  const { register, handleSubmit, formState: { errors } } = useForm();
  const navigate = useNavigate();

  const onSubmit = (data) => {
    console.log(data);
    axios.post("http://127.0.0.1:8000/register/", {
    username: data.username,
    email: data.email,
    password: data.password,
    first_name: data.first_name,
    last_name: data.last_name
     })
      .then(res => {
        console.log(res);
        console.log(res.data);
        if (res.data == "email has been sent") {
          alert("Email with verification link has been sent");
          navigate('/')
        }
      }).catch (function (error) {
        if (error.response.data.username) {
          alert("Such username already exists");
          console.log(1);
        };
        if (error.response.data.email) {
          alert("Profile with such email already exists");
          console.log(2);
        }
        
      })
    
    console.log(data);


  };




  return (
    
    <form onSubmit={handleSubmit(onSubmit)} style={{ maxWidth: '600px', margin: 'auto'}}>
      <label style={{color: "white"}}>Username</label>
      <input type="username" {...register("username", { required: true })} />
      {errors.username && <p>Username is required</p>}

      <label style={{color: "white"}}>First name</label>
      <input type="first_name" {...register("first_name", { required: true })} />
      {errors.first_name && <p>Username is required</p>}

      <label style={{color: "white"}}>Last name</label>
      <input type="last_name" {...register("last_name", { required: true })} />
      {errors.last_name && <p>Username is required</p>}

      <div class="row mb-3">
      <label for="inputEmail3" class="col-sm-2 col-form-label" style={{color: "white"}}>Email</label>
      <div class="col-sm-10">
        <input type="email" {...register("email", { required: true, pattern: /^\S+@\S+$/i })} class="form-control" id="inputEmail3"/>
      </div>
      {errors.email && <p>Email is required and must be valid</p>}
      </div>

      <label style={{color: "white"}}>Password</label>
      <input type="password" {...register("password", { required: true })} />
      {errors.password && <p>Password is required</p>}

      <button type="submit">Submit</button>
    </form>
    
  );
}

export default Register;