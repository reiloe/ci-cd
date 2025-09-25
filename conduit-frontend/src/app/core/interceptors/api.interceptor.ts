import { Injectable } from "@angular/core";
import {
  HttpEvent,
  HttpInterceptor,
  HttpHandler,
  HttpRequest,
} from "@angular/common/http";
import { Observable } from "rxjs";

declare global {
  interface Window {
    __env: {
      apiUrl: string;
    };
  }
}

@Injectable({
  providedIn: "root",
})
export class ApiInterceptor implements HttpInterceptor {
  intercept(
    req: HttpRequest<any>,
    next: HttpHandler
  ): Observable<HttpEvent<any>> {
    const apiBaseUrl = window.__env?.apiUrl || "http://localhost:8000";

    const apiReq = req.clone({
      url: `${apiBaseUrl}/api${req.url}`,
    });

    return next.handle(apiReq);
  }
}
