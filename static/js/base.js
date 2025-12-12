class NavBar extends HTMLElement {
  constructor() {
    super();

    const logoutUrl = this.getAttribute("logout-url");
    const csrfToken = this.getAttribute("csrf-token");

    this.innerHTML = `
      <nav class="navbar">
          <div class="nav_logo">Testing Components</div>
          <ul class="nav-links">
              <li><a href="#">Home</a></li>
              <li>
                <form action="${logoutUrl}" method="POST">
                  <input type="hidden" name="csrfmiddlewaretoken" value="${csrfToken}">
                  <button type="submit" class="nav-link-btn">Logout</button>
                </form>
              </li>
          </ul>
      </nav>
      <div class="nav-spacer"></div>
    `;
  }
}

customElements.define('nav-bar', NavBar);
