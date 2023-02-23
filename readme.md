Django URL Shortener
--------------------

This is a simple Django URL shortener application that allows you to shorten long URLs into shorter, more manageable links.

### Getting Started

To get started, you will need to have Docker and Docker Compose installed on your system. If you do not have them installed, you can download them from the official websites:

-   Docker: <https://www.docker.com/get-docker>
-   Docker Compose: <https://docs.docker.com/compose/install/>

Once you have Docker and Docker Compose installed, follow these steps:

1.  Clone the repository to your local machine:

    ```bash
    git clone https://github.com/housemateguy/djangolinkshortner.git
    ```

2.  Change into the project directory:

    ```bash
    cd djangolinkshortner
    ```

3.  Run Docker Compose to build and start the application:

    ```bash
    docker-compose up # or sudo docker-compose up
    ```

4.  Open your web browser and go to `http://localhost:8000` to access the application: 

![Screenshot of the application](https://raw.githubusercontent.com/housemateguy/djangolinkshortner/master/imgs/Screenshot_2023-02-23_17-27-54.png)
    

### Creating Short URLs

To create a shortened URL, follow these steps:

1.  Go to `http://localhost:8000` in your web browser.
2.  Enter the long URL that you want to shorten in the input field.
4.  Set an expiration date or a click limit for the link.
5.  Click the "Shorten URL" button.
6.  You will be redirected to a new page that displays the shortened URL stats.

### Viewing Short URLs

To view a shortened URL that you have created, follow these steps:

1.  Go to `http://localhost:8000/stats/{short_url}` in your web browser.

### Screenshots

![Screenshot of the application](https://raw.githubusercontent.com/housemateguy/djangolinkshortner/master/imgs/Screenshot_2023-02-23_17-27-54.png)

![Screenshot of the application](https://raw.githubusercontent.com/housemateguy/djangolinkshortner/master/imgs/Screenshot_2023-02-23_17-28-23.png)

![Screenshot of the application](https://raw.githubusercontent.com/housemateguy/djangolinkshortner/master/imgs/Screenshot_2023-02-23_17-27-27.png)