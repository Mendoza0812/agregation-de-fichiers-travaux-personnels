<?php

$doctype = DOMImplementation::createDocumentType('html');
$dom = DOMImplementation::createDocument(null, 'html', $doctype);
$html = $dom->documentElement;
$html->head = $dom->createElement('head');
$html->appendChild($html->head);
$html->head->title = $dom->createElement('title');
$html->head->title->nodeValue = 'Exemple de HTML';
$html->head->appendChild($html->head->title);
$html->head->charset = $dom->createElement('meta');
$html->head->charset->setAttribute('http-equiv', 'Content-Type');
$html->head->charset->setAttribute('content', 'text/html; charset=utf-8');
$html->head->appendChild($html->head->charset);
$html->body = $dom->createElement('body');
$html->appendChild($html->body);
$html->body->p = $dom->createElement('p');
$html->body->p->nodeValue = 'Ceci est un paragraphe.';
$html->body->appendChild($html->body->p);
$html->body->p->br = $dom->createElement('br');
$html->body->p->appendChild($html->body->p->br);
$html->body->p->a = $dom->createElement('a');
$html->body->p->a->nodeValue = 'Ceci est un lien.';
$html->body->p->a->setAttribute('href', 'cible.html');
$html->body->p->appendChild($html->body->p->a);

echo $dom->saveHTML();
