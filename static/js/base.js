class NavBar extends HTMLElement {
  constructor() {
    super();

    const logoutUrl = this.getAttribute("logout-url");
    const csrfToken = this.getAttribute("csrf-token");
    const character_list_url = this.getAttribute('character_list_url');

    this.innerHTML = `
      <nav class="navbar">
          <div class="nav_logo">Testing Components</div>
          <ul class="nav-links">
              <li><a href="${character_list_url}">Home</a></li>
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




class LargeCard extends HTMLElement {
  constructor() {
    super();

    const h1 = this.getAttribute('h1');
    const characterUrl = this.getAttribute('character-url');

    this.innerHTML = `
    <div class = 'large_card'>
      <h1>${h1}</h1>
      <a href="${characterUrl}">Details</a>
    </div>
      `;
  }
}
customElements.define('large-card', LargeCard);

