package com.myra.assistant;

import android.app.Activity;
import android.os.Bundle;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.webkit.WebSettings;
import android.widget.LinearLayout;
import android.widget.TextView;
import android.widget.EditText;
import android.widget.Button;
import android.graphics.Color;
import android.text.InputType;
import android.content.SharedPreferences;

public class MainActivity extends Activity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        SharedPreferences prefs = getSharedPreferences("myra", MODE_PRIVATE);
        LinearLayout layout = new LinearLayout(this);
        layout.setOrientation(LinearLayout.VERTICAL);
        layout.setPadding(16, 16, 16, 16);
        layout.setBackgroundColor(Color.rgb(15, 10, 22));

        TextView title = new TextView(this);
        title.setText("MYRA AI Assistant");
        title.setTextSize(24);
        title.setTextColor(Color.WHITE);
        layout.addView(title);

        EditText serverInput = new EditText(this);
        serverInput.setSingleLine(true);
        serverInput.setHint("Server URL");
        serverInput.setText(prefs.getString("server", "http://127.0.0.1:8765"));
        layout.addView(serverInput);

        EditText tokenInput = new EditText(this);
        tokenInput.setSingleLine(true);
        tokenInput.setHint("MYRA token");
        tokenInput.setInputType(InputType.TYPE_CLASS_TEXT | InputType.TYPE_TEXT_VARIATION_PASSWORD);
        layout.addView(tokenInput);

        Button button = new Button(this);
        button.setText("Connect to MYRA");
        layout.addView(button);

        TextView note = new TextView(this);
        note.setText("Pehle Termux mein MYRA server chalayen.");
        note.setTextColor(Color.LTGRAY);
        layout.addView(note);

        button.setOnClickListener(v -> {
            String server = serverInput.getText().toString().trim();
            String token = tokenInput.getText().toString().trim();
            while (server.endsWith("/")) server = server.substring(0, server.length() - 1);

            if (server.isEmpty() || token.isEmpty()) {
                note.setText("Server URL aur token dono enter karein.");
                return;
            }

            prefs.edit().putString("server", server).apply();
            String url = server + "/?t=" + android.net.Uri.encode(token);

            WebView web = new WebView(this);
            WebSettings settings = web.getSettings();
            settings.setJavaScriptEnabled(true);
            settings.setDomStorageEnabled(true);
            web.setWebViewClient(new WebViewClient());
            setContentView(web);
            web.loadUrl(url);
        });

        setContentView(layout);
    }
}
